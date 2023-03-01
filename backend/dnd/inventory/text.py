# import inspect
# import sys
# import weapon
# classes = [cls_name for cls_name, cls_obj in
#            inspect.getmembers(sys.modules['weapon']) if
#            inspect.isclass(cls_obj)]
#
# print(classes)
#
# import ast
#
# for im in ast.walk(ast.parse(open('weapon.py').read())):
#     if isinstance(im, ast.ClassDef):
#         print(im.name)
import inspect
import weapon

for name, obj in inspect.getmembers(weapon):
    # if inspect.isclass(obj):
    #     print(obj)
    if inspect.isclass(obj):
        # x = obj()
        # print(x.info())
        if obj.__name__ in ('SimpleRangedWeapon', 'SimpleWeapon',
                            'MilitaryHandToHandWeapon',
                            'MilitaryRangedWeapons'):
            pass
        else:
            print(obj)
