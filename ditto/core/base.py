import docker

from ditto.core.results import extract_result_from_container_into_host


class BaseTool:
    image = None
    prefix_cmd = None

    def __init__(self):
        self.client = docker.from_env()
        self.new_cmd = []
        self.volumes = None
        self.container = None

    def run(self, cmd, current_dir):
        print("build-cmd")
        self.build_cmd(cmd)
        print("build-volume")
        self.build_volumes()
        print("run-container")
        self.run_container()
        print("patch-logs")
        self.patch_logs()
        print("handle-output")
        self.handle_output()

    def build_cmd(self, cmd):
        for i in cmd:
            if i.startswith("/"):
                self.new_cmd.append("/host" + i)
            else:
                self.new_cmd.append(i)

    def build_volumes(self):
        self.volumes = {
            '/': {'bind': '/host', 'mode': 'ro'},
        }

    def run_container(self):
        new_cmd = ' '.join(self.new_cmd)
        self.container = self.client.containers.run(
            self.image,
            f"{self.prefix_cmd} {new_cmd}",
            detach=True,
            volumes=self.volumes,
        )

    def patch_logs(self):
        for line in self.container.logs(stream=True):
            print(line.strip().decode().replace("/data", "/fake/path"))

    def handle_output(self):
        extract_result_from_container_into_host(self.container.id, ".")
