import os
import docker


class BaseTool:
    image = None
    prefix_cmd = None

    def __init__(self):
        self.client = docker.from_env()
        self.new_cmd = []
        self.volumes = None
        self.container = None

    def run(self, cmd, current_dir):
        self.build_cmd(cmd)
        self.build_volumes(current_dir)
        self.run_container()
        self.patch_logs(current_dir)

    def build_cmd(self, cmd):
        for i in cmd:
            if i.startswith("/"):
                self.new_cmd.append("/host" + os.path.abspath(i))
            elif i.startswith("./"):
                self.new_cmd.append("/host" + os.path.abspath(i))
            elif i.startswith("../"):
                self.new_cmd.append("/host" + os.path.abspath(i))
            else:
                self.new_cmd.append(i)

    def build_volumes(self, current_dir):
        self.volumes = {
            '/': {'bind': '/host', 'mode': 'rw'},
            current_dir: {'bind': '/data', 'mode': 'rw'},
        }

    def run_container(self):
        new_cmd = ' '.join(self.new_cmd)
        self.container = self.client.containers.run(
            self.image,
            f"{self.prefix_cmd} {new_cmd}",
            detach=True,
            volumes=self.volumes,
            user="1000:1000"
        )

    def patch_logs(self, current_dir):
        for line in self.container.logs(stream=True):
            line = line.strip().decode()
            # line = line.replace("/data", current_dir)
            # line = line.replace("/host", "")
            print(line)
