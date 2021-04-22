from ui.core import update_frenemies_info


def update_entity_display():
    # push to the ui
    frenemies_text = create_frenemies_text()
    update_frenemies_info(frenemies_text)
