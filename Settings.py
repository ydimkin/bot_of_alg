from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: SecretStr
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


config = Settings()


language = (
    "Python",
    "Rust",
    "C++",
    "JavaScript",
    "Java"
)

python_al = (
    "python_quick_sort",
    "python_binary_search",
    "python_bubble_sort",
    "python_dijkstra",
    "python_DFS"
)

rust_al = (
    "rust_quick_sort",
    "rust_binary_search",
    "rust_bubble_sort",
    "rust_dijkstra",
    "rust_DFS"
)

java_al = (
    "java_quick_sort",
    "java_binary_search",
    "java_bubble_sort",
    "java_dijkstra",
    "java_DFS"
)

c_plus_plus_al = (
    "c_quick_sort",
    "c_binary_search",
    "c_bubble_sort",
    "c_dijkstra",
    "c_DFS"
)

javascript_al = (
    "javascript_quick_sort",
    "javascript_binary_search",
    "javascript_bubble_sort",
    "javascript_dijkstra",
    "javascript_DFS"
)

alg = (
    "quick_sort",
    "binary_search",
    "bubble_sort",
    "dijkstra",
    "DFS"
)
