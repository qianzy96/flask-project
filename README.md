# flask-project
#learning flask
#相对导入与绝对导入
# myapp/views.py

# An absolute import gives us the User model
from myapp.models import User

# A relative import does the same thing
from .models import User
