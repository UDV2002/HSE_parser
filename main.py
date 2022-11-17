import typer
import db_manager

app = typer.Typer()


@app.command()
def show_faculties(parameter):
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
        print('[INFO] Error! Some of arguments is not correct')


@app.command()
def show_bachelor_courses(parameter):
    parameters = {'names': 'name', 'links': 'link', 'durations': 'duration', 'languages': 'language',
                  'campuses': 'campus', 'places': 'places', 'educationfroms': 'education_form'}
    sql_string = ''

    parameter_array = (parameter.split('-'))
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


@app.command()
def show_magister_courses(parameter):
    parameters = {'names': 'name', 'links': 'link', 'durations': 'duration', 'languages': 'language',
                  'campuses': 'campus', 'places': 'places', 'educationfroms': 'education_form'}
    sql_string = ''

    parameter_array = (parameter.split('-'))
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


if __name__ == '__main__':
    print('App is running')
    app()

