from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
import datetime
import pytz

class PdfCreator:

    @staticmethod
    def generate_structured_receipt(recipient_id, sender_id, amount, output_filename, logo_path):
        c = canvas.Canvas(output_filename, pagesize=letter)
        width, height = letter

        logo = ImageReader(logo_path)

        logo_width_top = 60
        logo_height_top = 60
        logo_x_top = 50
        logo_y_top = height - logo_height_top - 50

        c.drawImage(logo, logo_x_top, logo_y_top, width=logo_width_top, height=logo_height_top, mask='auto')

        margin = 50
        start_x = margin
        start_y = height - logo_height_top - 100

        c.setFont("Helvetica-Bold", 16)
        c.drawString(start_x, start_y, "Payment Receipt")

        c.setLineWidth(2)
        c.setStrokeColor(colors.black)
        c.line(start_x, start_y - 10, width - margin, start_y - 10)

        c.setFont("Helvetica", 12)

        current_utc_date = datetime.datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

        def draw_field(label, value, x, y, field_width, field_height):
            c.setLineWidth(1)
            c.setStrokeColor(colors.gray)
            c.rect(x, y - field_height, field_width, field_height, fill=0)

            c.drawString(x + 5, y - 15, f"{label}: {value}")

        field_width = width - 2 * margin
        field_height = 30
        y_position = start_y - 50

        draw_field("Date", current_utc_date, start_x, y_position, field_width, field_height)
        y_position -= field_height + 10

        draw_field("Sender ID", sender_id, start_x, y_position, field_width, field_height)
        y_position -= field_height + 10

        draw_field("Recipient ID", recipient_id, start_x, y_position, field_width, field_height)
        y_position -= field_height + 10

        draw_field("Amount", f"{amount:.2f} $", start_x, y_position, field_width, field_height)
        y_position -= field_height + 20

        c.drawString(start_x, y_position - 30, "Thank you for using FastPay!")

        logo = ImageReader(logo_path)

        logo_width = 100
        logo_height = 100
        logo_x = width - margin - logo_width
        logo_y = (y_position + 20) - logo_height // 2

        c.saveState()
        c.setFillAlpha(0.15)
        c.drawImage(logo, logo_x, logo_y, width=logo_width, height=logo_height, mask='auto')
        c.restoreState()

        c.save()