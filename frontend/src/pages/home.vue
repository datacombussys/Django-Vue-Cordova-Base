<template>
  <f7-page name="home">
    <!-- Top Navbar -->
    <f7-navbar :sliding="false" titleLarge title="Associated Builders and Contractors of Southern California!">
       <f7-nav-right>
      <f7-link icon-ios="f7:lock" icon-aurora="f7:lock" icon-md="f7:lock" panel-open="left"></f7-link>
        <f7-link icon-ios="f7:lock_open" icon-aurora="f7:lock_open" icon-md="f7:lock_open" login-screen-open="#my-login-screen"></f7-link>
      </f7-nav-right>
    </f7-navbar>

    <!-- Tabbar Begin-->
    <f7-subnavbar>
      <f7-segmented tag="p">
        <f7-button fill color="gray" href="/">Home Page</f7-button>
        <f7-button fill color="gray" href="/summary/">Summary Page</f7-button>
        <f7-button fill color="gray" href="/checkout/">Checkout Page</f7-button>
        <f7-button fill color="gray" href="/admin/">Admin Page</f7-button>
      </f7-segmented>
    </f7-subnavbar>

    <!-- Toolbar-->
    <f7-toolbar bottom>
      <f7-link>Privacy Policy</f7-link>
      <f7-link>Terms and Conditions</f7-link>
    </f7-toolbar>
    <!-- Page content-->
    <f7-block-title medium>Enter Wizard here</f7-block-title>
 
 
    <f7-block-title>Tabs Go Here</f7-block-title>
    <f7-block>
      <f7-row>
        <f7-col width="50">
          <f7-button fill raised href="/">Anaheim</f7-button>
        </f7-col>
        <f7-col width="50">
          <f7-button fill raised href="/">Ventura</f7-button>
        </f7-col>
      </f7-row>
    </f7-block>
    
    <f7-block>
      <f7-row>
        <f7-col>
          <p>This is where I will place the classes using a v-if statement</p>
          <p>I can use a table with sections from Buelfy</p>
        </f7-col>
      </f7-row>
    </f7-block>

    <f7-block>
      <f7-row>
        <f7-col>
          <p>text here</p>
        </f7-col>
      </f7-row>
    </f7-block>


    <f7-block>
      <f7-row>
        <f7-col width="50">
          <f7-button fill color="red" href="/" view=".view-main">Previous</f7-button>
        </f7-col>
        <f7-col width="50">
          <f7-button fill color="green" href="/" view=".view-main">Next</f7-button>
        </f7-col>
      </f7-row>
    </f7-block>


  </f7-page>
</template>