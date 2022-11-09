import typer
import db_manager

app = typer.Typer()


@app.command()
def show_faculties():
    db_manager.print_table_data('*', 'faculties', "")


@app.command()
def show_bachelor_courses():
    db_manager.print_table_data('*', 'bachelor_courses', '')


if __name__ == '__main__':
    app()
