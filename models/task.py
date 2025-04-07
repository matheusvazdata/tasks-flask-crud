class Task:
    def __init__(self, id, title, description, completed=False) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        """
        Serializa a instância para um dicionário.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }

    def __repr__(self):
        """
        Representação legível da tarefa, útil para logs e debug.
        """
        return f"<Task {self.id}: {self.title}, Completed: {self.completed}>"