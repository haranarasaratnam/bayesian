BOOKS = {
    'book1': {
        'title': 'Estimation',
        'chapters': {
            'ch1': {
                'title': 'Chapter 1: Introduction',
                # 'template': 'books/book1/ch1.html',
                'subchapters': {
                    'ch1_1': {
                        'title': '1.1: Probabilty and Bayes\' Rule',
                        'template': 'books/book1/ch1_1.html'
                    },
                    'ch1_2': {
                        'title': '1.2: Kalman Filtering',
                        'template': 'books/book1/ch1_2.html'
                    },
                    'ch1_3': {
                        'title': '1.3: Use Case 1: Estimation  with DC Motor',
                        'template': 'books/book1/ch1_3.html'
                    },
                }
            },
            'ch2': {
                'title': 'Chapter 2: Nonlinear Gaussian Filters',
                # 'template': 'books/book1/ch2_1.html'
                'subchapters': {
                    'ch2_1': {
                        'title': '2.1: Extended Kalman Filters',
                        'template': 'books/book1/ch2_1.html'
                    },
                    'ch2_2': {
                        'title': '2.2: Unscented Kalman Filters',
                        'template': 'books/book1/ch2_2.html'
                    },
                    'ch2_3': {
                        'title': '2.3: Gauss-Hermite Kalman Filters',
                        'template': 'books/book1/ch2_3.html'
                    },
                    'ch2_4': {
                        'title': '2.4: Cubature Kalman Filters',
                        'template': 'books/book1/ch2_4.html'
                    },
                    'ch2_5': {
                        'title': '2.5: Use Case 1: Radar Tracking',
                        'template': 'books/book1/ch2_5.html'
                    },
                    'ch2_6': {
                        'title': '2.6: Use Case 2: Mobile Robot Navigation',
                        'template': 'books/book1/ch2_6.html'
                    },
                }
            },

            'ch3': {
                'title': 'Chapter 3: Nonlinear Non-Gaussian Filters',
                # 'template': 'books/book1/ch2_1.html'
                'subchapters': {
                    'ch3_1': {
                        'title': '3.1: Particle Filters',
                        'template': 'books/book1/ch3_1.html'
                    },
                    'ch3_2': {
                        'title': '3.2: Use Case 1: SLAM',
                        'template': 'books/book1/ch3_2.html'
                    },
                }
            },

            'ch4': {
                'title': 'Chapter 4: Variants',
                # 'template': 'books/book1/ch2_1.html'
                'subchapters': {
                    'ch4_1': {
                        'title': '4.1: Square-root Filters',
                        'template': 'books/book1/ch4_1.html'
                    },
                    'ch4_2': {
                        'title': '4.2: Information Filters',
                        'template': 'books/book1/ch4_2.html'
                    },
                    'ch4_3': {
                        'title': '4.3: Smoothers',
                        'template': 'books/book1/ch4_3.html'
                    },
                    'ch4_4': {
                        'title': '4.4: Continuous-Discrete Filters',
                        'template': 'books/book1/ch4_4.html'
                    },
                }
            },

            'ch5': {
                'title': 'Chapter 5: Practical Considerations',
                # 'template': 'books/book1/ch2_1.html'
                'subchapters': {
                    'ch5_1': {
                        'title': '5.1: Estimation under unknown model and noise statistics',
                        'template': 'books/book1/ch5_1.html'
                    },
                    'ch5_2': {
                        'title': '5.2: Filter Initialization',
                        'template': 'books/book1/ch5_2.html'
                    },
                    'ch5_3': {
                        'title': '5.3: Combining Multiple Models Using IMM Filter',
                        'template': 'books/book1/ch5_3.html'
                    },
                },
            },

            'ch6': {
                'title': 'Chapter 6: Suggested Readings',
                # 'template': 'books/book1/ch2_1.html'
                'subchapters': {
                    'ch6_1': {
                        'title': '6.1: References',
                        'template': 'books/book1/ch6_1.html'
                    },
                },
            },
        }, #chaps
    },

    'book2': {
        'title': 'Control',
        'chapters': {
            'ch1': {
                'title': 'Chapter 1: Getting Started',
                'template': 'books/book2/ch1.html',
                'subchapters': {
                    'ch1_1': {
                        'title': '1.1: Basics',
                        'template': 'books/book2/ch1_1.html'
                    }
                }
            }
        }
    },

    'book3': {
        'title': 'Coding',
        'chapters': {
            'ch1': {
                'title': 'Chapter 1: Getting Started',
                'template': 'books/book2/ch1.html',
                'subchapters': {
                    'ch1_1': {
                        'title': '1.1: Basics',
                        'template': 'books/book2/ch1_1.html'
                    }
                }
            }
        }
    }

}
