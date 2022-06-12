from abc import ABC, abstractmethod
import random


class MatureLanguageFilterStrategy(ABC):
    @abstractmethod
    def modify(self, text: str, word: str) -> str:
        pass


class RemoveWordStrategy(MatureLanguageFilterStrategy):
    def modify(self, text: str, word: str) -> str:
        return text.replace(word, '')


class StarWordStrategy(MatureLanguageFilterStrategy):
    def modify(self, text: str, word: str) -> str:
        return text.replace(word, '*' * len(word))


class MessWordStrategy(MatureLanguageFilterStrategy):
    def modify(self, text: str, word: str) -> str:
        mess_word = word
        while mess_word == word:
            mess_word = ''.join(random.sample(word, len(word)))
        return text.replace(word, mess_word)


class LengthWordStrategy(MatureLanguageFilterStrategy):
    def modify(self, text: str, word: str) -> str:
        return text.replace(word, f'{"*" * int(len(word)/2)}{len(word)}{"*" * int(len(word)/2)}')


class MatureLanguageFilterStrategyProvider:
    def get_strategy(self, strategy_type: str) -> MatureLanguageFilterStrategy:
        if strategy_type.lower() == "remove":
            return RemoveWordStrategy()
        elif strategy_type.lower() == "star":
            return StarWordStrategy()
        elif strategy_type.lower() == "mess":
            return MessWordStrategy()
        elif strategy_type.lower() == 'length':
            return LengthWordStrategy()


if __name__ == "__main__":
    choice = input("Choose strategy [remove|star|mess|length]: ")
    text_to_filter = "Holy cow now I have to cow go there myself!"

    strategy = MatureLanguageFilterStrategyProvider().get_strategy(choice)
    output = strategy.modify(text_to_filter, "cow")
    print(output)
