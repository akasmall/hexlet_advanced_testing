# BEGIN (write your solution here)
class FakeClient():
    # Здесь мы описываем желаемые данные, которые должны вернуться в тесте
    def __init__(self, language):
        self.language = language

    # Возвращаем сами себя, чтобы иметь возможность вызвать get_repos()
    # по цепочке
    def list_for_users(self, name):
        # return self
        return self.language

# END


# !решение ментора
#
# ?# BEGIN
# *class FakeClient():
# *    def __init__(self, data):
#         """Set data to property."""
#         self.data = data

# *    def list_for_users(self, user_name):
#         return self.data
# ?# END
