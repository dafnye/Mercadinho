class User:
    # Simulação de um banco de dados
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com", "cnpj": "31.092.768/0001-66", "celular": "(11)95817-2821", "senha": "usuario1", "status": "inativo", "activation_code": None},
        {"id": 2, "name": "Bob", "email": "bob@example.com", "cnpj": "31.092.768/0001-66", "celular": "(11)95817-2821", "senha": "usuario2", "status": "inativo", "activation_code": None}
    ]
    
    @classmethod
    def get_users(cls):
        return cls.users
    
    @classmethod
    def get_user_by_id(cls, user_id):
        for user in cls.users:
            if user["id"] == user_id:
                return user
        return None

    @classmethod
    def store(cls, data):
        new_user = {
            "id": len(cls.users) + 1,
            "name": data["name"],
            "email": data["email"],
            "cnpj": data["cnpj"],
            "celular": data["celular"],
            "senha": data["senha"],
            "status": "inativo",  
            "activation_code": None 
        }
        cls.users.append(new_user)
        return new_user
    
    @classmethod
    def update_user(cls, user_id, data):
        user = cls.get_user_by_id(user_id)
        if user:
            user.update(data)
            return user
        return None

    @classmethod
    def delete_user(cls, user_id):
        user = cls.get_user_by_id(user_id)
        if user:
            cls.users.remove(user)
            return user
        return None
