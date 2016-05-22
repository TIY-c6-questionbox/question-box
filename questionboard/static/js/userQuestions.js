var $userquestions = $('#userquestions');
var $userquestlist = $('#userquestlist');
var $user = document.getElementById('user');



var $questionform = $('#questionform');
var $question = $('#question');
var $textarea = $('#textarea');
var $answertext = $('#answertext');
var $questionlist = $('#list');



// <li><a href='/question/'>Question 1</a></li>

$.get('/../../api/question/', function(questionlist){
  questionlist.results.forEach( function(question) {
  var $li = $('<li>')
  var pattern = new RegExp("question/[0-9]+")
  var tag = pattern.exec(question.url)
  link = '<a href="' + '/' + tag[0] + '">' + question.title + '</a>'
  $li.append(link)
  $li.appendTo($userquestlist)
})
})
