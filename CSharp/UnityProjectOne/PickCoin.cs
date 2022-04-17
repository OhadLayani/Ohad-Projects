using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;//for text
public class PickCoin : MonoBehaviour
{
    public AudioSource pickSound;
    public Text Coins;
    public Text info;
    //must be connected in unity 
    public static int numCoins=0;
    public static int CoinsNeeded = 3;
    public bool CoinCheck=false; 
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private void OnTriggerEnter(Collider other)
    {
        //Make object inactive-vanishing it for player
        this.gameObject.SetActive(false);
        pickSound.Play();
        numCoins=numCoins+1;
        CoinsNeeded = CoinsNeeded--;
        Coins.text = "Gold Coins : " + numCoins;
        info.text = "You need to collect " + CoinsNeeded + " coins ";
        if (numCoins >= 3)
        {
            //info.text = "";
            CoinCheck = true;
            info.text = "Something has been unlocked Find it!";


        }


    }

}
