(this.webpackJsonpclient=this.webpackJsonpclient||[]).push([[0],{38:function(e,t,c){"use strict";c.r(t);var n=c(2),s=c.n(n),r=c(12),a=c.n(r),i=c(14),l=c(0);var o=function(e){var t=e.search,c=e.loading,n=s.a.useRef();return Object(l.jsxs)("div",{class:"input-group",children:[Object(l.jsxs)("div",{class:"form-outline",children:[Object(l.jsx)("input",{type:"search",id:"form1",class:"form-control",ref:n}),Object(l.jsx)("label",{class:"form-label",for:"form1",children:"Search"})]}),Object(l.jsx)("button",{type:"button",class:"btn btn-primary",onClick:function(){return t(n.current)},children:c?Object(l.jsx)("div",{class:"spinner-border text-light",role:"status",children:Object(l.jsx)("span",{class:"visually-hidden",children:"Loading..."})}):Object(l.jsx)("i",{class:"fas fa-search"})})]})},j=c(13),d=c.n(j);var u=function(){var e=Object(n.useState)(!1),t=Object(i.a)(e,2),c=t[0],s=t[1];return Object(l.jsx)("div",{className:"text-center mt-5",children:Object(l.jsx)(o,{search:function(e){var t=e.value;s(!0),d.a.get("http://127.0.0.1:5000/api/search_topic/"+t).then((function(e){var t=e.data;s(!1),console.log(t)}))},loading:c})})};a.a.render(Object(l.jsx)(s.a.StrictMode,{children:Object(l.jsx)(u,{})}),document.getElementById("root"))}},[[38,1,2]]]);
//# sourceMappingURL=main.5ae20e54.chunk.js.map