import pynecone as pc


class State(pc.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index():
    return pc.hstack(
        pc.flex(
            pc.button(
                "Decrement",
                color_scheme="red",
                border_radius="1em",
                on_click=State.decrement,
            ),
            pc.heading(State.count, font_size="2em", margin_x="1em"),
            pc.button(
                "Increment",
                color_scheme="green",
                border_radius="1em",
                on_click=State.increment,
            ),
            margin_x="auto",
            padding="10rem"
        )
    )


app = pc.App(state=State)
app.add_page(index)
app.compile()