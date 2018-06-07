public class BGM : EActor
{
    public Container SoundContainer;

    private Sound SoundComponent = null;

    private bool SoundLoad = false;

    public override int Update()
    {
        if (SoundComponent==null)
       {
            SoundComponent = (Sound) SoundContainer.FindComponentByType("Sound");
       }

       if(SoundComponent !=null)
      {
           if (SoundLoad == false)
            {
                SoundComponent.PropSound.SetSoundFilePath("$project/Assets/wind.wav");
                SoundComponent.Play();
                Log("Sound Loaded", 0, 0.0f);
                SoundLoad = true;
            }
        }




        return 0;

    }

}
