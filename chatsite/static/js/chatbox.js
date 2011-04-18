function ISODateString(d) {
    function pad(n){
        return n<10 ? '0'+n : n;
    }
    return d.getUTCFullYear()+'-'
    + pad(d.getUTCMonth()+1)+'-'
    + pad(d.getUTCDate())+'T'
    + pad(d.getUTCHours())+':'
    + pad(d.getUTCMinutes())+':'
    + pad(d.getUTCSeconds())+'Z';
}

function create_connection(chatbox) {
  var conn = hookbox.connect('http://'+chatbox.hookbox_host+':'+chatbox.hookbox_port+'/');
  conn.onOpen = function() { 
    console.log("connection established!");
  };
  conn.onError = function(err) {
    console.log("connection failed: " + err.msg);
  };
  conn.onSubscribed = function(channel_name, subscription) {
    subscription.onPublish = function(frame) {
      console.log(frame);
    };
  };
  return conn;
}


var ChatMessage = Backbone.Model.extend({
  url: function() {
    return this.get('resource_uri') || this.collection.url;
  }
});

var ChatMessages = Backbone.Collection.extend({
  url: chatbox.messages_api,
  parse: function(data) {
    return data.objects;
  },
  localStorage: new Store("ChatMessages")
});

var ChatMessageView = Backbone.View.extend({
  tagName: 'li',
  classNmae: 'chat_message',

  render: function() {
      $(this.el).html(ich.message_template(this.model.toJSON()));
      $(this.el).find('abbr.timeago').timeago();
      return this;
  }
});

var App = Backbone.View.extend({
  el: $('#app'),
  events: {
    'click #send_message': 'sendMessage',
    'submit form': 'sendMessage',
  },
  initialize: function(subscription) {
    this.subscription = subscription;
    _.bindAll(this, 'addOne', 'addAll', 'render');
    this.messages = new ChatMessages();
    this.messages.bind('add', this.addOne);
    this.messages.bind('refresh', this.addAll);
    this.messages.bind('all', this.render);
    this.messages.fetch();
  },
  addAll: function() {
    this.messages.each(this.addOne);
  },
  addOne: function(chat_message) {
    var view = new ChatMessageView({model:chat_message});
    this.$('#messages').append(view.render().el);
  },
  sendMessage: function() {
    console.log("SendMessage");
    var message = this.$('#message_input').val();
    if (message) {
      this.subscription.publish(message);
      var new_date = new Date();
      this.messages.create({
        message: message,
        username: chatbox.user,
        "date": ISODateString(new_date)
      });
      this.$('#message_input').val('');
    }
    return false;
  }
});
