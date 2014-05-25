import datetime

NUMBERS = [-2, -1, 0, 0.3, 0.5, 0.8, 1, 2, 3, 4, 5, 6, 7, 8, 9]
AMBIGUOUS_CHARS = ['i', 'I', 'l', 'L', 'o', 'O', '1', '0', 'lI1oO0']
DESCENDERS = ['gjpyq']
DELIMITERS = ['()', '{}', '[]', '""']
OTHERS = ['!@#$%^&*-=_+\|`~',
          ';:,.<>?/',
          '--', '__', '~~', '++', '==', '##', '^^', '**', '((', '))']

class Hello(object):
    """
    >>> greeter = Hello('John')
    >>> greeter.greet()
    >>> 'Hello, John!'
    """
    def __init__(self, name):
        self.name = name

    def greet(self, name=None):
        print "Hello, %s!" % (name or self.name)

class Filler:
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam
    lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam
    viverra nec consectetur ante hendrerit. Donec et mollis dolor.
    Praesent et diam eget libero egestas mattis sit amet vitae augue.
    Nam tincidunt congue enim, ut porta lorem lacinia consectetur. Donec ut
    libero sed arcu vehicula ultricies a non tortor. Lorem ipsum dolor sit
    amet, consectetur adipiscing elit. Aenean ut gravida lorem. Ut turpis
    felis, pulvinar a semper sed, adipiscing id dolor. Pellentesque auctor
    nisi id magna consequat sagittis. Curabitur dapibus enim sit amet elit
    pharetra tincidunt feugiat nisl imperdiet. Ut convallis libero in urna
    ultrices accumsan. Donec sed odio eros. Donec viverra mi quis quam
    pulvinar at malesuada arcu rhoncus. Cum sociis natoque penatibus et
    magnis dis parturient montes, nascetur ridiculus mus. In rutrum
    accumsan ultricies. Mauris vitae nisi at sem facilisis semper ac in est.

    Vivamus fermentum semper porta. Nunc diam velit, adipiscing ut
    tristique vitae, sagittis vel odio. Maecenas convallis ullamcorper
    ultricies. Curabitur ornare, ligula semper consectetur sagittis, nisi
    diam iaculis velit, id fringilla sem nunc vel mi.
    """
