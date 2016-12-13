from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import markovify
import nltk
import re

class POSifiedText(markovify.Text):
	def word_split(self, sentence):
		words = re.split(self.word_split_pattern, sentence)
		words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
		return words

	def word_join(self, words):
		sentence = " ".join(word.split("::")[0] for word in words)
		return sentence

def index(request):
	return HttpResponse("Hello, world. You're at the teddy index.")

def start(request):
	template = loader.get_template('base.html')
	context  = {
		'foo': 'zizzz',
	}
	return HttpResponse(template.render(context, request))

def make(request):
	template = loader.get_template('base.html')
	src = request.POST.get('source', None)
	mark = markovify.Text(src, state_size=2)
	out = []
	for i in range(100):
		out.append(mark.make_sentence())

	context  = {
		'source': src,
		'xout': "\n".join(['<p>%s</p>' % sentence for sentence in out]),
		'out': out,
	}
	return HttpResponse(template.render(context, request))
