### Django Rest Framework-based system for Baseball Statistic Query

* The goal of this project is to provide an application which will run numpy/scipy/matplot functions in a Lambda instance

### Numpy Function Endpoint
`/numpy/`

Returns a dictionary containing the title, source code and JSON output

### drf_apis/drf_baseball

`admin.py`
* NumpyFunctionAdmin
* NumpyDataStructureInline

`models.py`
* NumpyFunction
* NumpyDataStructure

`views.py`
* NumpyFunctionViewset

`serializers`
* NumpyFunctionSerializer
* NumpyDataStructureSerializer

