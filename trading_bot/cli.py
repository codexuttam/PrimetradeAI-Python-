import click
from bot.orders import OrderManager
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import sys

console = Console()

@click.command()
@click.option('--symbol', required=True, help='Trading symbol (e.g., BTCUSDT)')
@click.option('--side', type=click.Choice(['BUY', 'SELL'], case_sensitive=False), required=True, help='Order side')
@click.option('--type', 'order_type', type=click.Choice(['MARKET', 'LIMIT'], case_sensitive=False), required=True, help='Order type')
@click.option('--quantity', required=True, type=float, help='Quantity to trade')
@click.option('--price', type=float, help='Price (required for LIMIT orders)')
def main(symbol, side, order_type, quantity, price):
    """
    Simplified Binance Futures Trading Bot CLI
    """
    console.print(Panel.fit("[bold blue]Binance Futures Trading Bot[/bold blue] (Testnet)", border_style="blue"))
    
    # Summary of Request
    table = Table(title="Order Submission Request")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="magenta")
    table.add_row("Symbol", symbol.upper())
    table.add_row("Side", side.upper())
    table.add_row("Type", order_type.upper())
    table.add_row("Quantity", str(quantity))
    table.add_row("Price", str(price) if price else "N/A")
    console.print(table)

    # Execute Order
    try:
        manager = OrderManager()
        result = manager.execute_order(symbol, side, order_type, quantity, price)

        if result["success"]:
            data = result["data"]
            console.print("[bold green]✔ Order Placed Successfully![/bold green]")
            
            # Response Details
            res_table = Table(title="Order Response Details")
            res_table.add_column("Field", style="cyan")
            res_table.add_column("Value", style="yellow")
            
            res_table.add_row("Order ID", str(data.get('orderId')))
            res_table.add_row("Status", str(data.get('status')))
            res_table.add_row("Executed Qty", str(data.get('executedQty')))
            res_table.add_row("Avg Price", str(data.get('avgPrice', 'N/A')))
            res_table.add_row("Symbol", str(data.get('symbol')))
            res_table.add_row("Type", str(data.get('type')))
            
            console.print(res_table)
        else:
            console.print("[bold red]✘ Order Placement Failed![/bold red]")
            for err in result["errors"]:
                console.print(f"[red]Error: {err}[/red]")
            sys.exit(1)

    except Exception as e:
        console.print(f"[bold red]Critical Error:[/bold red] {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
