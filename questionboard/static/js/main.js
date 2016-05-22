$.get('api/question/', function(questions){
    if (questions.results != undefined) {
        questions.results.forEach(for_function);
    }
})

function for_function(question) {
        var $li = $('<li>');
        $li.text(question.title);
        $li.appendTo($question);
}

var $questionform = $('#questionform');
var $question = $('#question');
var $textarea = $('#textarea');
var $answertext = $('#answertext');
var $questionlist = $('#list');

$questionform.submit(function() {
  console.log('Form submitted!');


  $.ajax({
    method: 'POST',
    url: 'api/question/',
    beforeSend: function(request) {
        var token = document.cookie.replace('csrftoken=', '')
        request.setRequestHeader('X-CSRFToken', token)
    },
    data: {
      title: $question.val(),
      description: $textarea.val(),
    },
    success: function(newQuestion) {
      console.log('test')
      var $li = $('<li>')
      var pattern = new RegExp("question/[0-9]+")
      var tag = pattern.exec(newQuestion.url)
    //   link = '<a href="' + tag + '">' + newQuestion.title + '</a>'
      link = '<a href="' + tag[0] + '">' + newQuestion.title + '</a>'
      $li.append(link)
      $li.appendTo($questionform)
      $li.appendTo($questionlist)
    },
  });

  return false;
});


// <li><a href='/question/'>Question 1</a></li>

$.get('api/question/', function(questionlist){
  questionlist.results.forEach( function(question) {
  var $li = $('<li>')
  var pattern = new RegExp("question/[0-9]+")
  var tag = pattern.exec(question.url)
  link = '<a href="' + tag[0] + '">' + question.title + '</a>'
  $li.append(link)
  $li.appendTo($questionlist)
})
})

function getQuestions() {
    $.get('api/question/', function(questions) {
        var results = questions.results;
        var question = null;

        for (var i in results) {
            var question = results[i];

            (function (question) {
                var $form = $('<form class="question" data-id="' + question.id + '">').appendTo(document.body)

                $('<p>').text(question.title).appendTo($form)


                $('<input type="submit" value="Delete"/>').appendTo($form)

                $form.submit(function() {
                    deleteQuestion(question.id);

                    return false;
                })
            }) (question);
        }
    })
}



var $answerform = $('#answerform');
var $answertext = $('#answertext');
var $questionobj = $('#questionobj');
var $user = $('#user');

$answerform.submit(function() {
  console.log($answerform);
  console.log($answertext.val());
  console.log($questionobj.val());
  console.log($user.val());
  console.log('api/users/'+ $user.val() + '/');




$.ajax({
  method: 'POST',
  url: 'api/answer/',
  beforeSend: function(request) {
      var token = document.cookie.replace('csrftoken=', '')
      request.setRequestHeader('X-CSRFToken', token)

  },
  data: {
    text: $answertext.val(),
    score: 0,
    question: 'api/question/'+ $questionobj.val() + '/',
    owner: 'api/users/' + $user.val() + '/',
  },

  success: function(newAnswer) {
    console.log('Answer Posted')
  }
});
  return false;
});







// function deleteQuestion(questionID) {
//     $.ajax({
//         method: 'DELETE',
//         url: '/question/' + questionID + '/',
//         beforeSend: function(request) {
//             var token = document.cookie.replace('csrftoken=', '')
//             request.setRequestHeader('X-CSRFToken', token)
//         }
//         success: function() {
//             var $question = $('.question[data-id=' + questionID + ']')
//             console.log('Question deleted', $question)
//             $question.remove();
//         }
//     })
//
// }
//
//
// function createCreateQuestionForm() {
//     var createQuestionForm = $('<form>')
//
//     $('<label for="title">Title</label><br>').appendTo(form)
//     var title = $('<input type="text" id="title"><br>').appendTo(form)
//
//     $('<label for="title">Title</label><br>').appendTo(form)
//     var title = $('<input type="text" id="title"><br>').appendTo(form)
//
//
//     $('<input type="submit" value="Create Question">').appendTo(form)
//
//     createQuestionForm.submit(function() {
//         console.log('Question created')
//         return false;
//     })
//     createQuestionForm.appendTo(document.body)
// }
