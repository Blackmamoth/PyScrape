from terminology import in_blue, in_red, in_bold


class ConsoleLogger:
    @staticmethod
    def info(text: str) -> None:
        print(in_blue(in_bold(f"[*] {text}")))

    @staticmethod
    def error(text: str) -> None:
        print(in_red(in_bold(f"[!] {text}")))
