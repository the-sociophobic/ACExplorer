import os

plugin_name = 'Export Binary'
plugin_level = 4
file_type = '*'


def plugin(app, file_id):
	data = app.tempNewFiles(file_id)
	if data is None:
		app.log.warn(__name__, "Failed to find file {:016X}".format(file_id))
		return
	out_file = open(
		os.path.join(
			app.CONFIG['dumpFolder'],
			f'{app.gameFunctions.gameIdentifier}_{data["fileName"]}_{file_id:016X}.bin'
		), 'wb'
	)
	out_file.write(data['rawFile'].read_rest())
