import logging
from baseoperation import BaseOperation


class ListOperation(BaseOperation):
    def __init__(self, group_id, args, output=None):
        super(ListOperation, self).__init__(group_id, args, {'output': output})

    def run(self, repo):
        # suppress logging
        logging.getLogger().disabled = True
        repo.load_all()
        logging.getLogger().disabled = False

        repo.print_list(self.output)
        return 0
