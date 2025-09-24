import os
import sys
import pandas as pd


def get_card_set_path(file_name: str) -> str:
    """

    :return:
    """
    cards_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(sys.argv[0])), 'cards'))
    file_path = os.path.join(cards_folder, file_name + '.csv')
    return file_path


def read_cards_from_csv(file_name: str) -> pd.DataFrame:
    """

    :param file_name:
    :return:
    """
    file_path = get_card_set_path(file_name)
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = pd.read_csv(file)
        return file_content


def add_terms_to_set(set_name: str, terms: list[str], descriptions: list[str], is_stared: list[bool]) -> None:
    """

    :param set_name:
    :param terms:
    :param descriptions:
    :param is_stared:
    :return:
    """
    file_path = get_card_set_path(set_name)
    # build DataFrame with new term
    new_term = pd.DataFrame({'term': terms, 'description': descriptions, 'is_stared': is_stared})
    # insert rows to csv file
    with open(file_path, 'a', encoding='utf-8') as file:
        new_term.to_csv(file, header=False, index=False, lineterminator='\n')


def get_all_files_from_dir():
    """

    :return:
    """
    cards_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(sys.argv[0])), 'cards'))
    files = list(map(lambda file: file.split('.')[0], os.listdir(cards_folder)))
    return files


def get_random_cards(cards_file: str, count: int):
    file_path = get_card_set_path(cards_file)
    with open(file_path, 'r', encoding='utf-8') as file:
        df = pd.read_csv(file)
        card_set = pd.DataFrame(df.sample(min(count, len(df)))).drop_duplicates()
        return card_set
