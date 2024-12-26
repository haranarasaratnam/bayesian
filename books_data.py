BOOKS = {
    'book1': {
        'title': 'Book One',
        'chapters': {
            'ch1': {
                'title': 'Chapter 1: Introduction',
                'template': 'books/book1/ch1.html',
                'subchapters': {
                    'ch1_1': {
                        'title': 'Section 1.1: Overview',
                        'template': 'books/book1/ch1_1.html'
                    },
                    'ch1_2': {
                        'title': 'Section 1.2: Details',
                        'template': 'books/book1/ch1_2.html'
                    }
                }
            },
            'ch2': {
                'title': 'Chapter 2: Advanced Topics',
                'template': 'books/book1/ch2.html'
            }
        }
    },
    'book2': {
        'title': 'Book Two',
        'chapters': {
            'ch1': {
                'title': 'Chapter 1: Getting Started',
                'template': 'books/book2/ch1.html',
                'subchapters': {
                    'ch1_1': {
                        'title': 'Section 1.1: Basics',
                        'template': 'books/book2/ch1_1.html'
                    }
                }
            }
        }
    }
}
