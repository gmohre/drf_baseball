### Django Rest Framework-based system for Baseball Statistic Query

* The goal of this project is to provide an application which will run numpy/scipy/matplot functions in a Lambda instance

### Numpy Function Endpoint
`/numpy/`

Returns a dictionary containing the title, source code, JSON output, and serialized NumpyDataStructures

### drf_apis/drf_baseball

`admin.py`
* NumpyFunctionAdmin
* NumpyDataStructureInline

`models.py`
* NumpyFunction
* NumpyDataStructure

`views.py`
* NumpyFunctionViewSet

`serializers`
* NumpyFunctionSerializer
* NumpyDataStructureSerializer

