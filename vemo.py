class Payment:
    def __init__(self, ammount, user_from, user_to, note):
        ...
    
    def __str__(self):
        return f"{self.user_from} paid {self.user_to} ${self.ammount} for {self.note}"

class User:
    def __init__(self, balance: float, name: str, cc_balance: float):
        self._cash_balance = balance
        self._credit_card = cc_balance
        self.name = name
        self.activity = []
        self.friends = []

    def pay(self, target_user, ammount, note):
        if self._cash_balance - ammount < 0:
            self._credit_card-= ammount - self._cash_balance
            self._cash_balance = 0 
        self._cash_balance -= ammount
        _activity = f"{str(self)} paid {str(target_user)} ${ammount} for {note}"
        self.append(_activity)
        MiniVemo.render_feed(_activity)
    
    def add_friend(self, new_friend):
        if new_friend not in self.friends:
            self.friends.append(new_friend)
        else:
            raise Exception("Already added as a friend")
    
    def retrieve_activity(self):
        ...
  
    
    def __str__(self):
        return self.name

class MiniVemo:
    def __init__(self):
        self.feed = {}
        self.users = []
    def create_user(self, name, starting_balance, cc):
        new_user = User(name=name, balance=starting_balance, credit_card=cc)
        if new_user not in self.users:
            self.users.append(new_user)
            return new_user
        else:
            raise Exception("Already created")
    
    @classmethod
    def render_feed(self, to_render):
        print(to_render)


if __main__ == "__name__":
    bob = MiniVemo.create_user(name="Bob", starting_balance=9999, credit_card=9999)
    carol = MiniVemo.create_user(name="Carol", starting_balance=9999, credit_card=9999)
    bob.add_friend(carol)
    bob.pay(carol, 10000, "Just because")
    
