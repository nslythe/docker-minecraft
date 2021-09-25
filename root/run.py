import time
import subprocess
import os
import go

class Run(go.BaseRunner):
    def __init__(self):
        self.process = None
        self.cwd = "/config"

    def description(self):
        return [
            "Minecraft application"
        ]

    def config(self):
        if not os.path.exists(self.cwd):
            os.makedirs(self.cwd, mode=0o777, exist_ok=True)

        config_process = subprocess.Popen(
            args = [
                "java",
                "-Xmx1024M",
                "-Xms1024M",
                "-jar", "/server.jar",
                "--initSettings",
            ],
            cwd = self.cwd
        )
        config_process.wait()

        if os.environ.get("EULA", "false").lower() == "true":
            with open(os.path.join(self.cwd, "eula.txt"), "w") as f:
                    f.write("eula=true")
        else:
            raise Exception("Define EULA env to accept minecraft eula\nhttps://www.minecraft.net/en-us/eula")


    def run(self):
        self.process = subprocess.Popen(
            args = [
                "java",
                "-Xmx1024M",
                "-Xms1024M",
                "-jar", "/server.jar",
                "--nogui",
                "--port", "25565",
                "--universe", "/config"
            ],
            cwd = self.cwd
        )
        return self.process.wait()

    def check(self):
        return self.process.poll()

    def stop(self):
        self.process.kill()
