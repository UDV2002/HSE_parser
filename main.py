import typer
import db_manager
from rich import print as rprint

app = typer.Typer()


@app.command()
def show_faculties(parameter: str):
    parameters = {'names': 'name', 'links': 'link'}
    sql_string = ''

    parameter_array = (parameter.split('-'))
    try:
        if len(parameter_array) > 1:
            for word in parameter_array:
                if word != parameter_array[-1]:
                    sql_string += parameters.get(word) + ', '
                else:
                    sql_string += parameters.get(word)
        else:
            if parameter != 'all':
                sql_string = parameters.get(parameter)
            else:
                sql_string = '*'
        db_manager.print_table_data(sql_string, 'faculties', '')

    except TypeError:
        rprint('[italic red][INFO] Error! Some of arguments are not correct[/italic red]')


@app.command()
def show_bachelor_courses(parameter: str):
    parameters = {'names': 'name', 'links': 'link', 'durations': 'duration', 'languages': 'language',
                  'campuses': 'campus', 'places': 'places', 'educationfroms': 'education_form'}
    sql_string = ''

    parameter_array = (parameter.split('-'))
    try:
        if len(parameter_array) > 1:
            for word in parameter_array:
                if word != parameter_array[-1]:
                    sql_string += parameters.get(word) + ', '
                else:
                    sql_string += parameters.get(word)
        else:
            if parameter != 'all':
                sql_string = parameters.get(parameter)
            else:
                sql_string = '*'
        db_manager.print_table_data(sql_string, 'bachelor_courses', '')
    except TypeError:
        rprint('[italic red][INFO] Error! Some of arguments are not correct[/italic red]')


@app.command()
def show_magister_courses(parameter: str):
    parameters = {'names': 'name', 'links': 'link', 'durations': 'duration', 'languages': 'language',
                  'campuses': 'campus', 'places': 'places', 'educationfroms': 'education_form'}
    sql_string = ''

    parameter_array = (parameter.split('-'))
    try:
        if len(parameter_array) > 1:
            for word in parameter_array:
                if word != parameter_array[-1]:
                    sql_string += parameters.get(word) + ', '
                else:
                    sql_string += parameters.get(word)
        else:
            if parameter != 'all':
                sql_string = parameters.get(parameter)
            else:
                sql_string = '*'
        db_manager.print_table_data(sql_string, 'magister_courses', '')
    except TypeError:
        rprint('[italic red][INFO] Error! Some of arguments are not correct[/italic red]')


if __name__ == '__main__':
    rprint('[italic green][INFO] App is running...[/italic green]')
    app()

