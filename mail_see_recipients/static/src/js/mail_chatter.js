odoo.define('ventus_mail.mail_chatter', function (require) {
"use strict";

var chat_manager = require('mail.chat_manager');
var composer = require('mail.composer');
var ChatThread = require('mail.ChatThread');
var utils = require('mail.utils');

var config = require('web.config');
var core = require('web.core');
var form_common = require('web.form_common');
var web_utils = require('web.utils');

var _t = core._t;
var QWeb = core.qweb;
var Mail_Chatter_new = core.form_widget_registry.get('mail_thread');

    /**
     * extended mail_thread to change the function open_composer
     **/
     
var Mail_Chatter_Mail = Mail_Chatter_new.extend({
    template: 'mail.Chatter',

    events: {
        "click .o_chatter_button_new_message": "on_open_composer_new_message",
        "click .o_chatter_button_log_note": "on_open_composer_log_note",
    },
    
    init: function () {
        this._super.apply(this, arguments);
        this.model = this.view.dataset.model;
        this.res_id = undefined;
        this.context = this.options.context || {};
        this.dp = new web_utils.DropPrevious();
    },

    willStart: function () {
        return chat_manager.is_ready;
    },
    
    // composer toggle
    on_open_composer_new_message: function () {
        this.open_composer_message();
    },
    
    open_composer_message: function (options) {
    	
    	this.followers = this.field_manager.fields.message_follower_ids;
        var self = this;
        
        /* updated default value in context */
        
        var context = {
                default_parent_id: self.id,
                partner_ids: this.followers.followers,
                sub: this.view.datarecord.display_name
            };
       if (self.context.default_model && self.context.default_res_id) {
                context.default_model = self.context.default_model;
                context.default_res_id = self.context.default_res_id;
            }
            
        /* open action to compose mail */
        
        self.do_action({
            type: 'ir.actions.act_window',
            res_model: 'mail.compose.message',
            view_mode: 'form',
            view_type: 'form',
            views: [[false, 'form']],
            target: 'new',
            context: context
        }, {
            on_close: function() {
                self.trigger('need_refresh');
                var parent = self.getParent();
                chat_manager.get_messages({model: parent.model, res_id: parent.res_id});
            },
        }).then(self.trigger.bind(self, 'close_composer'));
    }
  });

core.form_widget_registry.add('mail_thread', Mail_Chatter_Mail);

return Mail_Chatter_Mail;

});
