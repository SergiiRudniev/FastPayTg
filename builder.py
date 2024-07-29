import subprocess
import os

dockerhub_username = "sergiirudniev"
project_name = "fastpay"
push = True
args = "--platform=linux/arm64"
selectContainer = True

class DockerContainer:
    def __init__(self, DirectoryPath: str, Name: str) -> None:
        self.__DirectoryPath = DirectoryPath
        self.__Name = Name.lower()

    def Build(self) -> None:
        returned_output = subprocess.check_output(
            f"docker build -t {dockerhub_username}/{project_name}{self.__Name}:latest {self.__DirectoryPath} {"--push" if push else ""} {args}")
        print(returned_output.decode("utf-8"))


def builder(containers: list[DockerContainer]):
    for container in containers:
        container.Build()


def scanner() -> list[DockerContainer]:
    current_directory = os.getcwd()

    folders = [f for f in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, f))]
    containers = []
    for folder in folders:
        if folder[0] != "." and os.path.isfile(f"./{folder}/Dockerfile"):
            if selectContainer:
                if (True if input(f"Build \"{folder}\"? Y/n :") == "Y" else False):
                    containers.append(DockerContainer(f"./{folder}", folder))
            else:
                containers.append(DockerContainer(f"./{folder}", folder))
    return containers


if __name__ == "__main__":
    containers = scanner()
    builder(containers)
