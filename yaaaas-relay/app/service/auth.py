from app.schema.auth import LoginPayload


class AuthService():
    
    def auth_user(self, login_payload: LoginPayload):
        raise NotImplementedError()
    

auth_service: AuthService()