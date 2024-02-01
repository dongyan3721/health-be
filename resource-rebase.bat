@echo off
setlocal enabledelayedexpansion

set "file=%cd%\app\config\ApplicationProperties.py"
set "property_file=%cd%\resource\application.yaml"
set "rep=%property_file:\=/%"
set "replacement=APPLICATION_PROPERTIES = YamlReader('%rep%').original_data"

@echo on
set "pattern=APP.*data"

sed -i "s#%pattern%#%replacement%#g" "%file%"
@echo done

