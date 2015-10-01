# flask-project
#learning flask
#相对导入与绝对导入
# myapp/views.py

# An absolute import gives us the User model
from myapp.models import User

# A relative import does the same thing
from .models import User

#为你的应用程序使用单一模块是有益于快速项目。
#在你的应用程序中使用包是有益于含有视图，模型，表单以及其它组件的项目。
#蓝图是组织含有几个明显区别的组件的项目的一个很好的方式。
