import operator
import pprint

def sort_multi(collection, *keys):
	return sorted(collection, key=operator.itemgetter(*keys))

class FilterModule(object):
	def filters(self):
		return {
			'sort_multi': sort_multi
		}
