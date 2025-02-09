import Bussiness_Access_Layer
import Bussiness_Entities.Entities as Bent
class Node:
    def __init__(self, obj_ent=Bent.C_Family_Entities()):
        self.left = None
        self.name = obj_ent.get_name()
        self.age = obj_ent.get_age()
        self.right = None
class C_Bussiness_Logics:
    def __init__(self):
        self.root=None

