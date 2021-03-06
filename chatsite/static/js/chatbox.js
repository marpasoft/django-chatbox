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

var User = Backbone.Model.extend({
});

var UserList = Backbone.Collection.extend({
  localStorage: new Store("UserList")
});

var UserView = Backbone.View.extend({
    tagName: 'li',
    render: function() {
      var data = this.model.toJSON();
      data['cid'] = this.model.cid;
      $(this.el).html(ich.user_template(data));
      return this;
    }
});

var UserListView = Backbone.View.extend({
  el: $('#presence'),
  initialize: function(presence_list) {
    _.bindAll(this, 'addOne', 'removeOne', 'removeByName', 'addAll', 'render', 'removeAll', 'refresh');
    this.refresh(presence_list);
  },
  addAll: function() {
    this.users.each(this.addOne);
  },
  addOne: function(user) {
    var view = new UserView({model: user});
    $(this.el).append(view.render().el);
  },
  removeOne: function(model) {
    $(this.el).find('#user_'+model.cid).parent().remove();
  },
  refresh: function(presence_list) {
    if (this.users !== undefined) {
      this.removeAll();
    }
    this.users = new UserList();
    this.users.bind('add', this.addOne);
    this.users.bind('remove', this.removeOne);
    this.users.bind('refresh', this.addAll);
    this.users.bind('all', this.render);
    this.users.fetch();
    $this = this;
    _(presence_list).each(function(item) {
      var user = new User({'name': item});
      $this.users.add(user);
    });
  },
  removeAll: function() {
    this.users.each(this.removeOne);
  },
  removeByName: function(username) {
    var model = this.users.select(function(md) {
        return md.get('name') === username;
    })[0];
    if (model !== undefined) {
        this.users.remove(model);
    }
  }
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
    var presence_list = subscription.presence;
    this.presence = new UserListView(presence_list);
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
    var message = this.$('#message_input').val();
    if (message) {
      var new_date = ISODateString(new Date());

      this.subscription.publish({
          "message": message,
          "date": new_date
      });
      this.$('#message_input').val('');
    }
    return false;
  }
});
