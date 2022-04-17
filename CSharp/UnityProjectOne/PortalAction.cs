using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class PortalAction : MonoBehaviour
{
    public Animator animator;
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
        StartCoroutine(SceneSwitch());//run in parallel
    }


IEnumerator SceneSwitch()
    {
        //play fade in animation
        animator.SetBool("StartFadeIn", true);
        //delay
        yield return new WaitForSeconds(2);
        //SceneSwitch
        if (SceneManager.GetActiveScene().buildIndex == 0)
        {
            SceneManager.LoadScene(1);
        }
        if (SceneManager.GetActiveScene().buildIndex == 1)
        {
            SceneManager.LoadScene(0);
        }
    }

}
