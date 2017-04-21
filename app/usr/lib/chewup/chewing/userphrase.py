import ctypes
import ctypes.util

libchewing_name = ctypes.util.find_library('chewing')
libchewing = ctypes.CDLL(libchewing_name)

## https://docs.python.org/3/library/ctypes.html
libchewing.chewing_userphrase_has_next.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_uint)]
libchewing.chewing_userphrase_get.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint, ctypes.c_char_p, ctypes.c_uint]


def foreach (run):
	phrase_len = ctypes.c_uint(0)
	bopomofo_len = ctypes.c_uint(0)

	ctx = libchewing.chewing_new()

	## https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L523
	rtn = libchewing.chewing_userphrase_enumerate(ctx)

	# print(rtn)

	if rtn < 0:
		return 0

	## https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L525
	while libchewing.chewing_userphrase_has_next(ctx, phrase_len, bopomofo_len):

		phrase = ctypes.create_string_buffer(phrase_len.value)
		bopomofo = ctypes.create_string_buffer(bopomofo_len.value)
		libchewing.chewing_userphrase_get(ctx, phrase, phrase_len, bopomofo, bopomofo_len)

		run(phrase.value.decode(), bopomofo.value.decode())

	ctx = libchewing.chewing_delete(ctx)

	return 0

def find_all():
	phrase_len = ctypes.c_uint(0)
	bopomofo_len = ctypes.c_uint(0)


	ctx = libchewing.chewing_new()

	## https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L523
	rtn = libchewing.chewing_userphrase_enumerate(ctx)

	list = []

	if rtn < 0:
		return list

	# print(rtn)

	## https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L525
	while libchewing.chewing_userphrase_has_next(ctx, phrase_len, bopomofo_len):
		##print('')
		##print('phrase_len:', phrase_len)
		##print('bopomofo_len:', bopomofo_len)
		##print('phrase_len.value:', phrase_len.value)
		##print('bopomofo_len.value:', bopomofo_len.vaue)

		phrase = ctypes.create_string_buffer(phrase_len.value)
		bopomofo = ctypes.create_string_buffer(bopomofo_len.value)
		libchewing.chewing_userphrase_get(ctx, phrase, phrase_len, bopomofo, bopomofo_len)
		##print('phrase:', phrase.raw.decode())
		##print('bopomofo:', bopomofo.raw.decode())
		##print('phrase:', phrase.value.decode())
		##print('bopomofo:', bopomofo.value.decode())
		item = (str(phrase.value.decode()), bopomofo.value.decode())
		list.append(item)

	ctx = libchewing.chewing_delete(ctx)

	return list

def add(phrase, bopomofo):
	ctx = libchewing.chewing_new()

	## https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L531
	rtn = libchewing.chewing_userphrase_add(ctx, phrase.encode(), bopomofo.encode())

	ctx = libchewing.chewing_delete(ctx)

	return rtn


def remove(phrase, bopomofo):
	ctx = libchewing.chewing_new()

	## https://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L533
	rtn = libchewing.chewing_userphrase_remove(ctx, phrase.encode(), bopomofo.encode())

	ctx = libchewing.chewing_delete(ctx)

	return rtn


def lookup(phrase, bopomofo):
	ctx = libchewing.chewing_new()

	## hhttps://github.com/chewing/libchewing/blob/v0.4.0/include/chewingio.h#L535
	rtn = libchewing.chewing_userphrase_lookup(ctx, phrase.encode(), bopomofo.encode())

	ctx = libchewing.chewing_delete(ctx)

	return rtn
