BOOKS = {
    'book1': {
        'title': 'Estimation',
        'chapters': {
            'ch1': {
                'title': 'Chapter 1: Introduction',
                # 'template': 'books/book1/ch1.html',
                'subchapters': {
                    'ch1_1': {
                        'title': '1.1: Bayes Rule',
                        'template': 'books/book1/ch1_1.html'
                    },
                    'ch1_2': {
                        'title': '1.2: Kalman Filtering',
                        'template': 'books/book1/ch1_2.html'
                    },
                    'ch1_3': {
                        'title': '1.3: Estimating State of DC Motor',
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
                        'title': '4.2: Continuous-Discrete Bayesian Filters',
                        'template': 'books/book1/ch4_2.html'
                    },
                    'ch4_3': {
                        'title': '4.3: Smoothers',
                        'template': 'books/book1/ch4_3.html'
                    },
                    'ch4_4': {
                        'title': '4.4: Interacting Multiple Model (IMM) Filters',
                        'template': 'books/book1/ch4_4.html'
                    },
                }
            },

            'ch5': {
                'title': 'Chapter 5: Applicationss',
                # 'template': 'books/book1/ch2_1.html'
                'subchapters': {
                    'ch5_1': {
                        'title': '5.1:  Radar Tracking (Accompanied by Python and Matlab Code)',
                        'template': 'books/book1/ch5_1.html'
                    },
                    'ch5_2': {
                        'title': '5.2: Mobile Robot Navigation',
                        'template': 'books/book1/ch5_2.html'
                    }
            },

            'ch6': {
                'title': 'Chapter 6: Suggested Readings',
                # 'template': 'books/book1/ch2_1.html'
                'subchapters': {
                    'ch6_1': {
                        'title': '6.1: Regerences',
                        'template': 'books/book1/ch6_1.html'
                        },
                    }
                }
            }
        }
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
