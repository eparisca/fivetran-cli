import typer

import destination_cli
import group_cli
import group_user_cli
import private_link_cli
import system_key_cli

app = typer.Typer()

app.add_typer(destination_cli.app, name="destination")
app.add_typer(group_cli.app, name="group")
app.add_typer(group_user_cli.app, name="group-user")
app.add_typer(private_link_cli.app, name="private-link")
app.add_typer(system_key_cli.app, name="system-key")


if __name__ == "__main__":
    app()
