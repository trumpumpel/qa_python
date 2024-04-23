import pytest

from main import BooksCollector


def set_book_genre(genre):
    pass


class TestBooksCollector:

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Сияние')

        assert len(collector.books_genre) == 2

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')

        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.books_genre['Оно'] == 'Ужасы'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Сияние')
        collector.add_new_book('Туман')

        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Туман', 'Ужасы')

        assert len(collector.get_books_with_specific_genre('Ужасы')) == 3

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Трое в лодке')

        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Трое в лодке', 'Комедии')

        assert 'Оно' in collector.books_genre and 'Ужасы' == collector.books_genre['Оно']
        assert 'Трое в лодке' in collector.books_genre and 'Комедии' == collector.books_genre['Трое в лодке']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Трое в лодке')

        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Трое в лодке', 'Комедии')
        assert collector.get_books_for_children() == ['Трое в лодке']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Трое в лодке')

        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Трое в лодке', 'Комедии')

        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Трое в лодке')
        assert len(collector.favorites) == 2

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Трое в лодке')
        collector.add_new_book('Словарь Санты')

        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Трое в лодке', 'Комедии')
        collector.set_book_genre('Словарь Санты', 'Комедии')

        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Словарь Санты')
        collector.add_book_in_favorites('Трое в лодке')
        collector.delete_book_from_favorites('Словарь Санты')
        assert len(collector.favorites) == 2

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Трое в лодке')
        collector.add_new_book('Словарь Санты')

        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Трое в лодке', 'Комедии')
        collector.set_book_genre('Словарь Санты', 'Комедии')

        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Трое в лодке')
        collector.add_book_in_favorites('Словарь Санты')

        assert collector.get_list_of_favorites_books() == ['Оно', 'Трое в лодке', 'Словарь Санты']

    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Оно', 'Ужасы'),
            ('Трое в лодке', 'Комедии'),
            ('Девушка с татуировкой дракона', 'Детективы')
        ]
    )
    def test_set_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert genre in collector.books_genre.values()

    @pytest.mark.parametrize(
        'book_name_1, genre_1, book_name_2, genre_2, book_name_3, genre_3',
        [
            ('Оно', 'Ужасы', 'Трое в лодке', 'Комедии', 'Словарь Санты', 'Комедии'),
            ('Бравый солдат Швейк', 'Комедии', 'Сияние', 'Ужасы', 'Туман', 'Ужасы')
        ]
    )
    def test_get_list_of_favorites_books(self, book_name_1, genre_1, book_name_2, genre_2, book_name_3, genre_3):
        collector = BooksCollector()
        collector.add_new_book(book_name_1)
        collector.add_new_book(book_name_2)
        collector.add_new_book(book_name_3)

        collector.set_book_genre(book_name_1, genre_1)
        collector.set_book_genre(book_name_2, genre_2)
        collector.set_book_genre(book_name_3, genre_3)

        collector.add_book_in_favorites(book_name_1)
        collector.add_book_in_favorites(book_name_2)
        collector.add_book_in_favorites(book_name_3)

        assert collector.get_list_of_favorites_books() == [book_name_1, book_name_2, book_name_3]
