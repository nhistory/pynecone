import pynecone as pc

config = pc.Config(
    app_name="number_counting",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
