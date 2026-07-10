# install dbt-duckdb
pip install dbt-duckdb

# freeze and save dependencies to requirements.txt
pip freeze > requirements.txt
# initialize dbt project
dbt init <dbt-project-name>
# move to <dbt-project-name>
cd <dbt-project-name>
# test or debug dbt project
dbt debug
# move back to the main folder
cd ..
