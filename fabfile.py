from fabric import Connection, task


@task
def hello(ctx):
    print("Hello World")


@task
def deploy(ctx):
    with Connection(
        "HOST",
        user="USERNAME",
        connect_kwargs={"key_filename": "~/.ssh/your_key"}
    ) as c:
        with c.cd("/home/project/path/"):
            c.run("ls")