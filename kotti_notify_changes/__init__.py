def kotti_configure(settings):
    settings['pyramid.includes'] += ' kotti_notify_changes'


def includeme():
    pass