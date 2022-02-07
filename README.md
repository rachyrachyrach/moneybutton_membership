Moneybutton Membership simple and advance paywall.
=================
Using Moneybutton's API for OAuth! I created this as a "membership" nft. Holders of the nft are able to access all special content. Holders without the NFT can pay with money. Or use a token that they own. In the "advanced" code section, this will allow the user to make only 1 purchase.  When they revist the site later, they can still view the content without repaying.

 You will be using JavaScript, html and if you want to try the advance part, you'll need a database.  I use DynamoDB from AWS. We are using JavaScript to talk to Moneybutton's API and AWS for checking and writing to the database. 

The first section of this readme will show you how to use [tokens without needing a database](https://docs.moneybutton.com/docs/mb-html.html). This means the user's information is not saved. So they will have to use a new token each time they pay. 

[Want to try it out?](https://www.tennesseeohioparanormalsociety.com/membership/) Contact me for tokens on my [MollyMatch Discord](https://discord.gg/cFZPH8A3hW).

![TOPS token](/docs/images/tops_token.jpg)

[credit Nate](https://twitter.com/ACP_Nate)

- **What You Need**

    - [Moneybutton Docs](https://docs.moneybutton.com/)

    - [Moneybutton Account](https://www.moneybutton.com/)

    - A database (I used AWS DynamoDB)
        ![DynamoDB](/docs/images/DynamoDB.jpg)

    - Python scripts (I used AWS Lambda)
        ![Lambda](/docs/images/lambda.jpg)

    - Your website

    - [Tokens aka assets aka NFTS](https://bitcointoken.exchange/asset/6521/)

    - Moneybutton's Script in html. This was found in the [HTML documentation](https://docs.moneybutton.com/docs/mb-html.html).

`<script src="https://www.moneybutton.com/moneybutton.js"></script>`

##Set up your Moneybutton App

1. Login to your [Moneybutton](https://www.moneybutton.com/) account. 


2. Go to your [settings](https://www.moneybutton.com/settings).

![Moneybutton Apps](/docs/images/1moneybutton-apps.jpg)


3. Create a new app.

![Moneybutton Apps](/docs/images/4-createnewapp.jpg)


4. Name your app and input your URL and create your app.

![Moneybutton Apps](/docs/images/5-addname.jpg)


5. Describe your app. This text will appear when the user authorizes your access to their wallet.

![Moneybutton Apps](/docs/images/6-appdescription.jpg)



6. Input the redirect url. This is the page where you want the user to go back to after they authorize your access to their wallet. Please note the OAuth client secret. Do not reveal this to the public. This gives apps to access your account. 

![Moneybutton Apps](/docs/images/7-redirecturl.jpg)


7. Close your app. The example is the [Moneybutton onPayment feature](https://docs.moneybutton.com/docs/mb-javascript.html). We will be using the `onPayment` object. This allows us to create a paywall called `displayHiddenContent`. In the html file [membership.html](/membership.html) go to line 27. 

```
<div class="money-button"
	 data-client-identifier="66de26eba2b7f927e4005ac94b4f797e"
  	 data-to="49581@moneybutton.com"
	 data-div-to-show="members_content"
	 data-button-data="Thank you for paying with MeasureClothing token!"
	 data-button-id="fiat"
  	 data-amount=".001"
  	 data-currency="USD"
  	 data-on-payment="displayHiddenContent"
></div>
```


8.[membership.html](/membership.html) line 27 has `data-client-identifier="66de26eba2b7f927e4005ac94b4f797e"` Please replace `66de26eba2b7f927e4005ac94b4f797e` with your own Client Identifier that you created in step 3. 


9.  Lets go find your Client Identifier.  Go to your [apps](https://www.moneybutton.com/settings#_yourApps). Your Client Identifier will be a similar number you see in this example.

![Moneybutton Apps](/docs/images/8-clientid.jpg)



10. Put your Client Identifier in [membership.html](/membership.html) line 27. 
```
<div class="money-button"
	 data-client-identifier="Your Client Identifier number here"
  	 data-to="49581@moneybutton.com"
	 data-div-to-show="members_content"
	 data-button-data="Thank you for paying with MeasureClothing token!"
	 data-button-id="fiat"
  	 data-amount=".001"
  	 data-currency="USD"
  	 data-on-payment="displayHiddenContent"
></div>
```

11. `data-to`

Check out the other options in the div. You will want to replace your own Moneybutton address or any legacy address. You can also put in your HandCash paymail there. 
```
<div class="money-button"
	 data-client-identifier="Your Client Identifier number here"
  	 data-to="Your Moneybutton address or legacy address"
	 data-div-to-show="members_content"
	 data-button-data="Thank you for paying with MeasureClothing token!"
	 data-button-id="fiat"
  	 data-amount=".001"
  	 data-currency="USD"
  	 data-on-payment="displayHiddenContent"
></div>
```

12. `data-div-to-show="members_content"`

This is for the div html code.  Line 4 has a `div id="members_content"`

```
<div id="members_content" style="display:none" data-hidden-for-button-id="fiat">
```


13. When the person pays with a Moneybutton token. This code inside here will display. For example the person pays with a token and they will see a YouTube video after payment.

`members_content` is also used in the "advanced" code. This is found in line 148.

```
<div id="members_content" style="display:none" data-hidden-for-button-id="fiat">

		
		<iframe width="560" height="315" src="https://www.youtube.com/embed/07PDkL_4VH4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


	<a href="https://bitcointoken.exchange/asset/6521/" target="_blank" rel="noopener"><img src="https://www.ashcancomicspub.com/uploads/2/4/2/5/24254619/tops-bsvtoken_orig.png" alt="First NFT" title="TOPS NFT series 1"></a>
    <center>
        <br>You Have TOPS NFT!!!
    </center>
</div>
```

14. `data-hidden-for-button-id="fiat" data-currency="USD"`

This is for paying with USD. 





## "Advanced" code This part is unfinished


1. Lines 65 - 192 are "advanced" code. [membership.html](/membership.html) has JavaScript & Ajax inside. [paidquery_lambda_function.py](/paidquery_lambda_function.py) and [webhookentry_lamdafunction.py](/webhookentry_lamdafunction.py) have Python to connect to AWS. This is back end development because you need a server to run a database and the python code. We are using AWS because Wordpress.com is hard to add backend code like databases. Webhooks allow us to be sneaky and connect to a database through Wordpress.com. Wordpress.org allows backend. 


2. Line 56 reads the balance of the logged in Moneybutton wallet. [API v2 Get User Balances ](https://docs.moneybutton.com/docs/api/v2/api-v2-user-balances.html) shows examples and options. This is where we use the url: 


`https://www.moneybutton.com/api/v2/me/wallets/active/balances`



To get your Client ID and Secret go back to your [settings](https://www.moneybutton.com/settings). 

![Moneybutton Apps](/docs/images/2moneybutton-apps-permissions.jpg)


Select the app you created.


![Moneybutton Apps](/docs/images/3-mb-apps-list.jpg)


Find your OAuth client identifier and OAuth client secret.

![Moneybutton Apps](/docs/images/oauth_client_secret.jpg)



3. Line 131 Checks for your public OAuth Client identifier. It will redirect to my [TOPS Membership](https://www.tennesseeohioparanormalsociety.com/membership/) page if the person has the NFT in their wallet. This was the url you put in your [App](https://www.moneybutton.com/settings).

```
if (!('code' in query_strings)){
		do_redirect = true;
		redir_url = "https://www.moneybutton.com/oauth/v1/authorize?response_type=code&client_id=09a338342ad0ebe43f106f63d6383bb1&redirect_uri=https://www.tennesseeohioparanormalsociety.com/membership/&scope=" + oauth_scope + "&state=somesecurerandomstring";
		window.location.href = redir_url;
	}
```


4. Line 10 Add your Client Secret to webhookentry_lamdafunction.py. View your Client Secret and add your webhook url.

```
      if json_body['secret'] != "Your OAuth client secret here":
```
![Webhook](/docs/images/webhook.jpg)
