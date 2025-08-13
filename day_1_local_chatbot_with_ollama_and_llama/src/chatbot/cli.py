from rich.console import Console
from .client import OllamaClient
from .service import ChatService

console = Console()

def run_cli() -> None:
    client = OllamaClient()
    svc = ChatService(client)
    console.print(f"[bold green]Local Chatbot — model: {client.model}[/bold green]")
    console.print("[dim]Type 'exit' to quit\n")

    while True:
        try:
            text = console.input("[yellow]You:[/yellow] ")
        except (KeyboardInterrupt, EOFError):
            console.print("\n[red]Goodbye![/red]")
            break

        if text.strip().lower() in ("exit", "quit"):
            console.print("[red]Goodbye![/red]")
            break

        resp = svc.send(text)
